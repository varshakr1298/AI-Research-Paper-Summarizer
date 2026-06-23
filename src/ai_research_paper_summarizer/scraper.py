from playwright.async_api import async_playwright

from .config import ARXIV_URL
from .models import Paper


async def fetch_papers() -> list[Paper]:
    papers = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True
        )

        page = await browser.new_page()

        await page.goto(
            ARXIV_URL,
            wait_until="domcontentloaded"
        )

        title_elements = page.locator(
            ".list-title"
        )

        total = await title_elements.count()

        for i in range(total):
            title_element = title_elements.nth(i)

            title = (
                await title_element.text_content()
            ).replace(
                "Title:",
                ""
            ).strip()

            abs_url = await title_element.evaluate(
                """
                element => {
                    const dd = element.closest('dd');
                    const dt = dd?.previousElementSibling;
                    const link = dt?.querySelector(
                        'a[href*="/abs/"]'
                    );

                    return link
                        ? 'https://arxiv.org' + link.getAttribute('href')
                        : null;
                }
                """
            )

            if abs_url:
                papers.append(
                    Paper(
                        title=title,
                        url=abs_url
                    )
                )

        await browser.close()

    return papers