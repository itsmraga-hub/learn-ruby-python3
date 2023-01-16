def caesar_cipher(str, num)
  e_str = ''
  str.split('').each do |char|
    ascii = char.ord
    if ascii >= 65 && ascii <= 90
      temp = ascii + num
      if temp > 90
        temp = (temp - 90) + 65 - 1
        chr = temp.chr
        e_str += chr
      else
        chr = temp.chr
        e_str += chr
      end
    elsif char.ord >= 95 && char.ord <= 122
      temp = ascii + num
      if temp > 122
        temp = (temp - 122) + 65 - 1
        chr = temp.chr
        e_str += chr
      else
        chr = temp.chr
        e_str += chr
      end
    else
      e_str += char
    end
  end
  e_str
end

puts caesar_cipher("What a string!", 5)
puts caesar_cipher("Zz", 5)
puts caesar_cipher("aA", 2)
# => "Bmfy f xywnsl!"

# puts 'W'.ord
# puts 'z'.ord
# puts 'A'.ord
# puts 'a'.ord
# puts 'Z'.ord
# puts 97.chr

