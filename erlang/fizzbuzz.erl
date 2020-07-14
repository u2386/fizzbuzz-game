-module(fizzbuzz).

-export([fizzbuzz/1]).

fizzbuzz(N) when N =/= 0 ->
    fizzbuzz(N - 1),
    Saying = if N rem 3 == 0, N rem 5 == 0 -> "fizzbuzz";
		N rem 3 == 0 -> "fizz";
		N rem 5 == 0 -> "buzz";
		true -> integer_to_list(N)
	     end,
    io:format('~s~n', [Saying]);
fizzbuzz(_) -> true.
