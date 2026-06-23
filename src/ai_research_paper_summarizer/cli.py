import asyncio

from playwright.async_api import async_playwright

from .scraper import fetch_papers
from .summarizer import summarize
from .utils import save_summary


async def main():
    print("Fetching recent AI papers from arXiv...\n")

    papers = await fetch_papers()

    if not papers:
        print(
            "No papers found. "
            "Please try again later."
        )
        return

    print("Recent AI Papers\n")

    for i, paper in enumerate(
        papers,
        start=1
    ):
        print(
            f"{i}. {paper.title}"
        )

    while True:
        try:
            choice = int(
                input(
                    "\nChoose paper number: "
                )
            )

            if (
                1
                <= choice
                <= len(papers)
            ):
                break

            print(
                f"Please enter a number "
                f"between 1 and "
                f"{len(papers)}."
            )

        except ValueError:
            print(
                "Please enter a valid "
                "number."
            )

    selected = papers[
        choice - 1
    ]

    print(
        f"\nOpening:\n"
        f"{selected.title}\n"
    )

    print(
        "Fetching paper details...\n"
    )

    async with async_playwright() as p:
        browser = (
            await p.chromium.launch(
                headless=True
            )
        )

        page = (
            await browser.new_page()
        )

        await page.goto(
            selected.url,
            wait_until="domcontentloaded"
        )

        authors = (
            await page.locator(
                "div.authors"
            ).text_content()
        )

        if authors:
            authors = authors.replace(
                "Authors:",
                ""
            ).strip()
        else:
            authors = "Unknown"

        abstract = (
            await page.locator(
                "blockquote.abstract"
            ).text_content()
        )

        if abstract:
            abstract = abstract.replace(
                "Abstract:",
                ""
            ).strip()
        else:
            abstract = (
                "No abstract found."
            )

        await browser.close()

    content = f"""
    Authors:
    {authors}

    Abstract:
    {abstract}
    """

    print(
        "Generating summary using "
        "Ollama...\n"
    )

    summary = summarize(
        selected.title,
        content
    )

    markdown = f"""
    # {selected.title}

    **Authors:** {authors}

    {summary}
    """

    path = save_summary(
        selected.title,
        markdown
    )

    print(markdown)
    print(
        f"\nSummary saved to:\n"
        f"{path}"
    )


def run():
    asyncio.run(main())


if __name__ == "__main__":
    run()
