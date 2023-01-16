def string_partition(str, inner_str)
  # Write a function that returns an inner string contained in the current string
  # if str = 'January' => true if inner str say 'anuar' is contained in str
  output_arr = str.partition(inner_str)
  p output_arr
  if output_arr[1] == inner_str
    true
  else
    false
  end
end

p string_partition('January', 'nua')
