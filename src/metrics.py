from typing import List

def _lcs_len(a: List[str], b: List[str]) -> int:
    n, m = len(a), len(b)
    # dp[i][j] = LCS длина для a[:i], b[:j]
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            if a[i] == b[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    return dp[n][m]

def score_fn(gold: str, pred: str) -> float:
    gold_toks = gold.split()
    pred_toks = pred.split()

    # крайние случаи
    if not gold_toks and not pred_toks:
        return 1.0
    if not gold_toks or not pred_toks:
        return 0.0

    l = _lcs_len(gold_toks, pred_toks)
    if l == 0:
        return 0.0

    prec = l / len(pred_toks)
    rec  = l / len(gold_toks)
    return 2 * prec * rec / (prec + rec)
