function findContentChildren(g: number[], s: number[]): number {
  let i = 0,
    j = 0;
  let count = 0;

  g.sort((a, b) => +a - +b);
  s.sort((a, b) => +a - +b);

  while (i < g.length && j < s.length) {
    if (s[j] >= g[i]) {
      i++;
      j++;
      count++;
    } else {
      j++;
    }
  }

  return count;
}
