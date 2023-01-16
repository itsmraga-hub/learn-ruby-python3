class LogLineParser
  def initialize(line)
    @line = line
  end

  def message
    # raise 'Please implement the LogLineParser#message method'
    words = @line.split(":")
    words[1].strip
  end

  def log_level
    # raise 'Please implement the LogLineParser#log_level method'
    words = @line.split(":")
    words[0].slice(1, words[0].length - 2).strip.downcase
  end

  def reformat
    # raise 'Please implement the LogLineParser#reformat method'
    message + " " + "(" + log_level + ")"
  end
end

puts LogLineParser.new('[ERROR]: Invalid operation').message
puts LogLineParser.new("[WARNING]:  Disk almost full\r\n").message
puts LogLineParser.new('[ERROR]: Invalid operation').log_level
puts LogLineParser.new('[INFO]: Operation completed').reformat
