def substrings(str, dictionary)
  substring_hash = {}
  new_arr = dictionary.select { |word| str.include?(word) }
  new_arr.each do |word|
    substring_hash[word] = str.scan(word).length
  end
  substring_hash
end



dictionary = ["below","down","go","going","horn","how","howdy","it","i","low","own","part","partner","sit"]

puts substrings("below", dictionary)
# => { "below" => 1, "low" => 1 }

puts substrings("Howdy partner, sit down! How's it going?", dictionary)
# => { "down" => 1, "go" => 1, "going" => 1, "how" => 2, "howdy" => 1, "it" => 2, "i" => 3, "own" => 1, "part" => 1, "partner" => 1, "sit" => 1 }