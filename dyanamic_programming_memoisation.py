#dynamic programming
"""
Question->
  find the longest common sub sequence of two sequences ans     return the `len` of it
 -> example
 -> [s,e,(r),(e),n,d,(i),(p),(i),(t),(o),u,s]
 -> [p,(r),(e),c,(i),(p),(i),(t),a,t,i,(o),n]
 -> return len(reipito)
"""
#memoisation
def lcsmemo(seq1,seq2):
	memo = {}
	def recurse(idx1=0,idx2=0):
		key = (idx1,idx2)
		if key in memo:
			return memo[key]
		elif idx1 == len(seq1) or idx2 == len(seq2):
			memo[key] = 0
		elif seq1[idx1] == seq2[idx2]:
			memo[key] = 1 + recurse(idx1+1,idx2+1)
		else:
			memo[key] = max(recurse(idx1+1,idx2),recurse(idx1,idx2+1))
			return memo[key]
		return recurse(0,0)
		
#tabulation solution
def lcs_tb(seq1,seq2):
	n1,n2 = len(seq1+1),len(seq2+1)
	table = [[0 for x in range(n2)] for x in range(n1)]
	for i in range(n1):
		for j in range(n2):
			if seq1[i] == seq2[j]:
				table[i+1][j+1] = 1 + table[i][j]
			else:
				table[i+1][j+1] = max(table[i][j+1],table[i+1][j])
	return table[-1][-1]
				
