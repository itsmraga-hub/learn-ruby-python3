module SavingsAccount
  def self.interest_rate(balance)
    # raise 'Please implement the SavingsAccount.interest_rate method'
   if balance >= 0 && balance < 1000
    0.5
   elsif balance >= 1000 && balance < 5000
    1.621
   elsif balance >= 5000
    2.475
   else
    3.213
   end
  end

  def self.annual_balance_update(balance)
    # raise 'Please implement the SavingsAccount.annual_balance_update method'
    balance + (balance * (self.interest_rate(balance) / 100))
  end

  def self.years_before_desired_balance(current_balance, desired_balance)
    # raise 'Please implement the SavingsAccount.years_before_desired_balance method'
    count = 0
    while current_balance < desired_balance
      count += 1
      new_balance = (current_balance * (self.interest_rate(current_balance) / 100))
      current_balance += new_balance
    end
    count
  end
end

puts SavingsAccount.interest_rate(200.75)
puts SavingsAccount.annual_balance_update(200.75)
puts SavingsAccount.years_before_desired_balance(200.75, 214.88)
