class BirdCount
  def self.last_week
    # raise 'Please implement the BirdCount.last_week method'
    # birds = [0, 2, 5, 3, 7, 8, 4]
    return 0, 2, 5, 3, 7, 8, 4
  end

  def initialize(birds_per_day)
    # raise 'Please implement the BirdCount#initialize method'
    @birds_per_day = birds_per_day
  end

  def yesterday
    # raise 'Please implement the BirdCount#yesterday method'
    @birds_per_day[-2]
  end

  def total
    # raise 'Please implement the BirdCount#total method'
    @birds_per_day.reduce(0) { |a, b| a + b }
  end

  def busy_days
    # raise 'Please implement the BirdCount#busy_days method'
    count = 0
    @birds_per_day.each  do |day|
      if day >= 5
        count += 1
      end
    end
    count
  end

  def day_without_birds?
    # raise 'Please implement the BirdCount#day_without_birds method'
    @birds_per_day.each do |day|
      if day === 0
        return true
      end
    end
    false
  end
end

puts BirdCount.last_week

birds_per_day = [2, 5, 0, 7, 4, 1]
bird_count = BirdCount.new(birds_per_day)
puts bird_count.yesterday

birds_per_day = [2, 5, 0, 7, 4, 1]
bird_count = BirdCount.new(birds_per_day)
puts bird_count.total

birds_per_day = [2, 5, 0, 7, 4, 1]
bird_count = BirdCount.new(birds_per_day)
puts bird_count.busy_days

birds_per_day = [2, 5, 0, 7, 4, 1]
bird_count = BirdCount.new(birds_per_day)
puts bird_count.day_without_birds?