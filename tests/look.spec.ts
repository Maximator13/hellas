import { test, type Page } from '@playwright/test'

test.skip(!!process.env.CI, 'captures are reviewed locally')

async function capture(page: Page, name: string, project: string, wait = 3500) {
  await page.waitForTimeout(wait)
  await page.screenshot({ path: `test-results/look-${name}-${project}.png` })
}

async function showEra(page: Page, era: string) {
  await page.getByRole('button', { name: new RegExp(`^${era},`) }).click()
}

test('capture the main screens', async ({ page }, testInfo) => {
  test.setTimeout(180_000)
  const project = testInfo.project.name
  await page.goto('./')
  await page.locator('.eras__button').first().waitFor()
  await capture(page, 'home', project, 6000)
  await showEra(page, 'Âge du bronze égéen')
  await capture(page, 'bronze', project)
  await page.keyboard.press('PageDown')
  await capture(page, 'transition', project, 1300)
  await capture(page, 'ages-obscurs', project)
  await page.keyboard.press('PageDown')
  await capture(page, 'archaique', project)
  await page.keyboard.press('PageDown')
  await capture(page, 'classique', project)
  await page.keyboard.press('PageDown')
  await capture(page, 'hellenistique', project)
  await page.goto('./#/evenement/bataille-de-salamine')
  await capture(page, 'salamine', project, 6000)
  await page.goto('./#/evenement/bataille-de-gaugameles')
  await capture(page, 'gaugameles', project, 6000)
})
