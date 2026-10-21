export const SITE = {
  origin: 'https://maximator13.github.io',
  base: '/hellas/',
  name: 'Hellas',
  title: 'Hellas, de Mycènes à Cléopâtre',
  description:
    "Frise chronologique et carte interactives du monde grec, des palais mycéniens à la mort de Cléopâtre (30 av. J.-C.) : cités, royaumes, batailles, dates, niveau de certitude et sources.",
  repository: 'https://github.com/Maximator13/hellas',
  publisher: 'Maximator13',
} as const

export const SITE_URL = `${SITE.origin}${SITE.base}`

export const ANALYTICS: { goatcounterCode: string | null } = {
  goatcounterCode: null,
}
