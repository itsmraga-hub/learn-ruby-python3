def caesar_cipher(str, num)
  encrypted_str = ''
  str.split('').each do |ch|
    char_ascii_value = ch.ord
    if char_ascii_value >= 97 && char_ascii_value <= 122
      temp = char_ascii_value + num
      if temp > 122
        temp = (temp - 122) + 97 - 1
        chr = temp.chr
        encrypted_str += chr
      else
        chr = temp.chr
        encrypted_str += chr
      end
    elsif char_ascii_value >= 65 && char_ascii_value <= 90
      temp = char_ascii_value + num
      if temp > 90
        temp = (temp - 90) + 65 - 1
        chr = temp.chr
        encrypted_str += chr
      else
        chr = temp.chr
        encrypted_str += chr
      end
    else
      encrypted_str += ch
    end
  end
  encrypted_str
end

puts caesar_cipher("What a string!", 5)
puts caesar_cipher("Zz", 5)
puts caesar_cipher("aA", 2)
# => "Bmfy f xywnsl!"

# puts 'W'.ord
# puts 'z'.ord
# puts 'A'.ord
# puts 'Z'.ord
# puts 97.chr