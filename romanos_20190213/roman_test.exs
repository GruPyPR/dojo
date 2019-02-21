Code.require_file "roman.ex", __DIR__
ExUnit.start()
defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "roman I returns 1" do
    assert Roman.to_integer(I) == 1
  end

  test "roman V returns 5" do
    assert Roman.to_integer(V) == 5
  end

  test "roman X returns 10" do
    assert Roman.to_integer(X) == 10
  end

  test "roman L returns 50" do
    assert Roman.to_integer(L) == 50
  end

  test "roman C returns 100" do
    assert Roman.to_integer(C) == 100
  end

  test "roman D returns 500" do
    assert Roman.to_integer(D) == 500
  end

  test "roman M returns 1000" do
    assert Roman.to_integer(M) == 1000
  end

  test "roman II returns 2" do
    assert Roman.to_integer(II) == 2
  end

  test "roman III returns 3" do
    assert Roman.to_integer(III) == 3
  end

  test "roman VI returns 6" do
    assert Roman.to_integer(VI) == 6
  end

  test "roman IV returns 4" do
    assert Roman.to_integer(IV) == 4
  end

  test "roman XLII returns 4" do
    assert Roman.to_integer(XLII) == 42
  end

  test "roman XXXIV returns 34" do
    assert Roman.to_integer(XXXIV) == 34
  end

  test "roman MMXIX returns 2019" do
    assert Roman.to_integer(MMXIX) == 2019
  end
end
