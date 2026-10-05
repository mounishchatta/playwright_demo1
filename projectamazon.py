import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False
        )
        page = await browser.new_page()
        await page.goto("https://www.amazon.in")
        await page.wait_for_timeout(3000)
        await page.locator('a:has-text("Mobiles")').click()
        await page.locator("header[id='navbar-main'] li:nth-child(3) div:nth-child(1) a:nth-child(1) span:nth-child(1)").click()
        await page.locator("//div[@id='grid-row-2-col-0']//img[@alt='.']").click()
        await page.locator("//a[@title='DIVIJA STORE Wood Smart Multipurpose Foldable Laptop Table with Cup Holder, Study Table, Bed Table, Breakfast Table, Foldable and Portable/Ergonomic &amp; Rounded Edges/Non-Slip Legs (Black), 59 cm, 8 cm']//div[@class='a-section octopus-pc-item-hue-shield octopus-pc-item-image-background-v3']").click()
        await page.get_by_title('Add to Shopping Cart').click()
        await page.wait_for_timeout(3000)
        await page.locator('[name="proceedToRetailCheckout"]').click()
        await page.wait_for_timeout(3000)
        await page.get_by_role("textbox").fill("1234567890")
        await page.locator('input.a-button-input').click()
        await page.wait_for_timeout(3000)
        await page.close()
       # await browser.close()
asyncio.run(main())

