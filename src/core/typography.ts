const NO_BREAK_SPACE = String.fromCharCode(0x00a0)
const NARROW_NO_BREAK_SPACE = String.fromCharCode(0x202f)
const WORD_JOINER = String.fromCharCode(0x2060)

export function frenchSpacing(text: string): string {
  return text
    .replace(/(\d) (?=\d{3}\b)/g, `$1${NARROW_NO_BREAK_SPACE}`)
    .replace(/(\d) (av\.|apr\.) J\.-C\./g, `$1${NO_BREAK_SPACE}$2${NO_BREAK_SPACE}J.-C.`)
    .replace(/J\.-C\./g, `J.-${WORD_JOINER}C.`)
    .replace(/ ([;!?»])/g, `${NARROW_NO_BREAK_SPACE}$1`)
    .replace(/ :/g, `${NO_BREAK_SPACE}:`)
    .replace(/« /g, `«${NARROW_NO_BREAK_SPACE}`)
}
