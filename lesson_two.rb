class Lasagna
  EXPECTED_MINUTES_IN_OVEN = 40
  def remaining_minutes_in_oven(actual_minutes_in_oven)
    # raise 'Please implement the Lasagna#remaining_minutes_in_oven method'
    time_left = EXPECTED_MINUTES_IN_OVEN - actual_minutes_in_oven
    time_left
  end

  def preparation_time_in_minutes(layers)
    # raise 'Please implement the Lasagna#preparation_time_in_minutes method'
    time_layers = 2 * layers
    time_layers
  end

  def total_time_in_minutes(number_of_layers:, actual_minutes_in_oven:)
    # raise 'Please implement the Lasagna#total_time_in_minutes method'
    total_time = (number_of_layers * 2) + actual_minutes_in_oven
    total_time
  end
end

l = Lasagna.new
puts l.remaining_minutes_in_oven(10)
puts l.preparation_time_in_minutes(3)
puts l.total_time_in_minutes(number_of_layers: 3, actual_minutes_in_oven: 20)
