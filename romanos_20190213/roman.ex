defmodule Roman do
  def to_integer(I), do: 1
  def to_integer(V), do: 5
  def to_integer(X), do: 10
  def to_integer(L), do: 50
  def to_integer(C), do: 100
  def to_integer(D), do: 500
  def to_integer(M), do: 1000
  def to_integer(x) do
    list = to_list(x)
    convert(list, 0)
  end

  defp to_list(x) do
    [_, string] = String.split(Atom.to_string(x), ".")
    String.codepoints(string)
  end

  defp get_value(numeral) do 
    to_integer(String.to_atom("Elixir." <> numeral))
  end


  defp convert([first | [ second | tail] ], accumulator) do
    cond do
      get_value(first) >= get_value(second) -> convert([second | tail], accumulator) + get_value(first)
      get_value(first) < get_value(second) ->  convert([second | tail], accumulator) - get_value(first)
    end
  end

  defp convert([first | tail], accumulator) do
    get_value(first) + convert(tail, accumulator) 
  end

  defp convert([], accumulator) do
    accumulator
  end
end
