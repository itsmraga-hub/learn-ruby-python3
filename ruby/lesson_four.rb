class Attendee
  def initialize(height)
    @height = height
  end

  def issue_pass!(pass_id)
    @pass_id = pass_id
  end

  def revoke_pass!
    @pass_id = nil
  end

  # Do not edit above methods, add your own methods below.

  def has_pass?
    # raise 'Please implement the Attendee#haspass? method'
    if @pass_id
      return true
    else
      return false
    end
  end

  def fits_ride?(ride_minimum_height)
    # raise 'Please implement the Attendee#fits_ride? method'
    if @height >= ride_minimum_height
      true
    else
      false
    end
  end

  def allowed_to_ride?(ride_minimum_height)
    # raise 'Please implement the Attendee#allowed_to_ride? method'
    if @pass_id && @height >= ride_minimum_height
      true
    else
      false
    end
  end
end

puts Attendee.new(100).has_pass?
puts Attendee.new(140).fits_ride?(100)
attendee = Attendee.new(100)
attendee.issue_pass!(42)
puts attendee.allowed_to_ride?(120)