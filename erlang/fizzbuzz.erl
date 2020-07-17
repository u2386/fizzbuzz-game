-module(fizzbuzz).

-export([fizzbuzz/1]).

fizzbuzz(N) when N =/= 0 ->
	fizzbuzz(N-1),
	saying(N);

fizzbuzz(_) -> true.

saying(N) when N rem 3 == 0, N rem 5 == 0 ->
	io:format('~p,~s~n', [N, "fizzbuzz"]);
saying(N) when N rem 3 == 0 ->
	io:format('~p,~s~n', [N, "fizz"]);
saying(N) when N rem 5 == 0 ->
	io:format('~p,~s~n', [N, "buzz"]);
saying(N) ->
	io:format('~s~n', [integer_to_list(N)]).
