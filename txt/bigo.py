a = 4
def rec(ind_Left, err_Left):
	if ind_Left == 0:
		return 1
	if err_Left == 0:
		return 1 + rec(ind_Left - 1, 0)
	return 1 + (a-1)*rec(ind_Left-1, err_Left-1) + rec(ind_Left-1, err_Left)
	
	
rec(0, E) --> O(1)
rec(L, 0) --> O(L)

rec(1, 1) --> O( 1 + a*O(rec(0, 0))  + rec(0, 1)      )
			  O( 1 + a*O(rec(0, 0))  + 1      )
			  O( 1 + a*1  + 1      )
			  O( a )
			  
rec(2, 1) --> O( 1 + a*O(rec(0, 0))  + rec(1, 1)      )
			  O( 1 + a*O(rec(0, 0))  + a      )
			  O( 1 + a*1  + a      )
			  O( 2a )
			  
rec(L, 1) --> O( La )

rec(1, 2) --> O(1 + (a-1)*rec(0, 1) + rec(0, 2))
          --> O(1 + a*O(1) + 1)
          --> O( a )


rec(1, 3) --> O(1 + (a-1)*rec(0, 2) + rec(0, 3))
          --> O(1 + a*O(1) + O(1))
          --> O( a )
		  
rec(1, E) --> O( a )

rec(2, 2) --> 1 + (a-1)*rec(1, 1) + rec(1, 2)
          --> 1 + a*O(a) + a
		  --> O( a^2 )

rec(2, 3) --> 1 + (a-1)*rec(1, 2) + rec(1, 3)
          --> 1 + a*O(a) + O(a)
          --> O( a^2 )
		  
rec(2, E) --> O( a^2 )

rec(3, 2) --> 1 + a*rec(2, 1) + rec(2, 2)
          --> 1 + a*O(a^2) + O(a^2)
		  --> O( a^3 )
		  
rec(3, 3) --> 1 + a*rec(2, 2) + rec(2, 3)
          --> 1 + a*O(a^2) + O(a^2)
		  --> O( a^3 )
		  
rec(L, E) --> O( a^L )