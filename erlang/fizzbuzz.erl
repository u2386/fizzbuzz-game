-module(fizzbuzz).

-export([fizzbuzz/1]).

fizzbuzz(N) -> fizzbuzz(N, spec()).

fizzbuzz(0, _) -> ok;
fizzbuzz(N, R) -> fizzbuzz(N - 1, R), R(N).

spec() ->
    R0 = all([times(3), times(5)]),
    R = any([rule(R0, saying("fizzbuzz")),
	     rule(times(3), saying("fizz")),
	     rule(times(5), saying("buzz")),
	     rule(always(), saying())]),
    fun (N) -> R(N) end.

any([]) -> fun (_) -> false end;
any(L) -> fun (N) -> any(N, L) end.

any(_, []) -> false;
any(N, [H | T]) ->
    case H(N) of
      true -> true;
      false -> any(N, T)
    end.

all([]) -> fun (_) -> false end;
all(L) -> fun (N) -> all(N, L) end.

all(_, []) -> true;
all(N, [H | T]) ->
    case H(N) of
      true -> all(N, T);
      false -> false
    end.

times(X) -> fun (N) -> N rem X =:= 0 end.

always() -> fun (_) -> true end.

rule(Pred, Action) ->
    fun (N) ->
	    case Pred(N) of
	      true -> Action(N), true;
	      false -> false
	    end
    end.

saying() -> fun (N) -> io:format("~B~n", [N]) end.

saying(X) -> fun (_) -> io:format("~s~n", [X]) end.
