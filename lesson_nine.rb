class BoutiqueInventory
  def initialize(items)
    @items = items
  end

  def item_names
    # raise 'Implement the BoutiqueInventory#item_names method'
    item_names_arr = []
    items.each do |item|
      item_names_arr.push(item[:name])
    end
    item_names_arr
  end

  def cheap
    # raise 'Implement the BoutiqueInventory#cheap method'
    cheap_items_arr = []
    items.each do |item|
      if item[:price] < 30
        cheap_items_arr.push(item)
      end
    end
    cheap_items_arr
  end

  def out_of_stock
    # raise 'Implement the BoutiqueInventory#out_of_stock method'
    stock_items_arr = []
    items.each do |item|
      if item[:quantity_by_size].empty?()
        stock_items_arr.push(item)
      end
    end
    stock_items_arr
  end

  def stock_for_item(name)
    # raise 'Implement the BoutiqueInventory#stock_for_item method'
    items.each do |item|
      if item[:name] === name
        return item[:quantity_by_size]
      end
    end
  end

  def total_stock
    # raise 'Implement the BoutiqueInventory#total_stock method'
    items_arr = []
    items.each do |item|
      item_arr = item[:quantity_by_size].map { |_, amt| amt }
      items_arr.push(item_arr)
    end
    items_arr.flatten.sum
  end

  private
  attr_reader :items
end

puts BoutiqueInventory.new([
  {price: 65.00, name: "Maxi Brown Dress", quantity_by_size: {s: 3, m: 7, l: 8, xl: 4}},
  {price: 50.00, name: "Red Short Skirt", quantity_by_size: {}},
  {price: 29.99, name: "Black Short Skirt", quantity_by_size: {s: 1, xl: 4}},
  {price: 20.00, name: "Bamboo Socks Cats", quantity_by_size: {s: 7, m: 2}}
]).item_names

puts BoutiqueInventory.new([
  {price: 65.00, name: "Maxi Brown Dress", quantity_by_size: {s: 3, m: 7, l: 8, xl: 4}},
  {price: 50.00, name: "Red Short Skirt", quantity_by_size: {}},
  {price: 29.99, name: "Black Short Skirt", quantity_by_size: {s: 1, xl: 4}},
  {price: 20.00, name: "Bamboo Socks Cats", quantity_by_size: {s: 7, m: 2}}
]).cheap

puts BoutiqueInventory.new([
  {price: 65.00, name: "Maxi Brown Dress", quantity_by_size: {s: 3, m: 7, l: 8, xl: 4}},
  {price: 50.00, name: "Red Short Skirt", quantity_by_size: {}},
  {price: 29.99, name: "Black Short Skirt", quantity_by_size: {s: 1, xl: 4}},
  {price: 20.00, name: "Bamboo Socks Cats", quantity_by_size: {s: 7, m: 2}}
]).out_of_stock

puts BoutiqueInventory.new([
  {price: 65.00, name: "Maxi Brown Dress", quantity_by_size: {s: 3, m: 7, l: 8, xl: 4}},
  {price: 50.00, name: "Red Short Skirt", quantity_by_size: {}},
  {price: 29.99, name: "Black Short Skirt", quantity_by_size: {s: 1, xl: 4}},
  {price: 20.00, name: "Bamboo Socks Cats", quantity_by_size: {s: 7, m: 2}}
]).stock_for_item("Black Short Skirt")

puts BoutiqueInventory.new([
  {price: 65.00, name: "Maxi Brown Dress", quantity_by_size: {s: 3, m: 7, l: 8, xl: 4}},
  {price: 50.00, name: "Red Short Skirt", quantity_by_size: {}},
  {price: 29.99, name: "Black Short Skirt", quantity_by_size: {s: 1, xl: 4}},
  {price: 20.00, name: "Bamboo Socks Cats", quantity_by_size: {s: 7, m: 2}}
]).total_stock
