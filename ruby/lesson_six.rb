class AssemblyLine
  def initialize(speed)
    @speed = speed
  end

  def production_rate_per_hour
    # raise 'Please implement the AssemblyLine#production_rate_per_hour method'
   if @speed == 10
    @speed * 221.0 * 77  / 100.0
   elsif @speed == 9
    @speed * 221.0 * 80  / 100.0
   elsif @speed >= 5 && @speed <= 8
    @speed * 221.0 * 90  / 100.0
   elsif @speed >= 1 && @speed <= 4
    @speed * 221.0
   end
  end

  def working_items_per_minute
    # raise 'Please implement the AssemblyLine#working_items_per_minute method'
    (production_rate_per_hour / 60.0).to_i
  end
end

puts AssemblyLine.new(6).production_rate_per_hour
puts AssemblyLine.new(6).working_items_per_minute
