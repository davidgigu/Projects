using System;
using System.Collections.Generic;

namespace InventoryManagement
{
    class Program
    {
        static InventoryManager inventoryManager = new InventoryManager();

        static void Main(string[] args)
        {
            Console.WriteLine("Inventory Management System");

            while (true)
            {
                Console.WriteLine();
                Console.WriteLine("1. Add Product");
                Console.WriteLine("2. Remove Product");
                Console.WriteLine("3. Update Product Details");
                Console.WriteLine("4. View Inventory");
                Console.WriteLine("5. Exit");
                Console.Write("Enter your choice: ");

                string choice = Console.ReadLine();

                switch (choice)
                {
                    case "1":
                        AddProduct();
                        break;
                    case "2":
                        RemoveProduct();
                        break;
                    case "3":
                        UpdateProductDetails();
                        break;
                    case "4":
                        ViewInventory();
                        break;
                    case "5":
                        Console.WriteLine("Exiting the application...");
                        return;
                    default:
                        Console.WriteLine("Invalid choice. Please try again.");
                        break;
                }
            }
        }

        static void AddProduct()
        {
            Console.WriteLine("Adding a new product");

            Console.Write("Enter the product ID: ");
            string id = Console.ReadLine();

            Console.Write("Enter the product name: ");
            string name = Console.ReadLine();

            Console.Write("Enter the product price: ");
            decimal price = decimal.Parse(Console.ReadLine());

            Console.Write("Enter the product quantity: ");
            int quantity = int.Parse(Console.ReadLine());

            inventoryManager.AddProduct(new Product(id, name, price, quantity));

            Console.WriteLine("Product added successfully.");
        }

        static void RemoveProduct()
        {
            Console.WriteLine("Removing a product");

            Console.Write("Enter the product ID: ");
            string id = Console.ReadLine();

            if (inventoryManager.RemoveProduct(id))
            {
                Console.WriteLine("Product removed successfully.");
            }
            else
            {
                Console.WriteLine("Product not found.");
            }
        }

        static void UpdateProductDetails()
        {
            Console.WriteLine("Updating product details");

            Console.Write("Enter the product ID: ");
            string id = Console.ReadLine();

            if (inventoryManager.ProductExists(id))
            {
                Console.Write("Enter the new product name: ");
                string name = Console.ReadLine();

                Console.Write("Enter the new product price: ");
                decimal price = decimal.Parse(Console.ReadLine());

                Console.Write("Enter the new product quantity: ");
                int quantity = int.Parse(Console.ReadLine());

                inventoryManager.UpdateProduct(new Product(id, name, price, quantity));

                Console.WriteLine("Product details updated successfully.");
            }
            else
            {
                Console.WriteLine("Product not found.");
            }
        }

        static void ViewInventory()
        {
            Console.WriteLine("Viewing inventory");

            List<Product> inventory = inventoryManager.GetInventory();

            if (inventory.Count == 0)
            {
                Console.WriteLine("Inventory is empty.");
            }
            else
            {
                Console.WriteLine("Current Inventory:");
                foreach (Product product in inventory)
                {
                    Console.WriteLine(product);
                }
            }
        }
    }

    class Product
    {
        public string ID { get; set; }
        public string Name { get; set; }
        public decimal Price { get; set; }
        public int Quantity { get; set; }

        public Product(string id, string name, decimal price, int quantity)
        {
            ID = id;
            Name = name;
            Price = price;
            Quantity = quantity;
        }

        public override string ToString()
        {
            return $"ID: {ID}, Name: {Name}, Price: {Price}, Quantity: {Quantity}";
        }
    }

    class InventoryManager
    {
        private List<Product> inventory = new List<Product>();

        public void AddProduct(Product product)
        {
            inventory.Add(product);
        }

        public bool RemoveProduct(string id)
        {
            Product product = inventory.Find(p => p.ID == id);

            if (product != null)
            {
                inventory.Remove(product);
                return true;
            }

            return false;
        }

        public bool ProductExists(string id)
        {
            return inventory.Exists(p => p.ID == id);
        }

        public void UpdateProduct(Product updatedProduct)
        {
            Product product = inventory.Find(p => p.ID == updatedProduct.ID);

            if (product != null)
            {
                product.Name = updatedProduct.Name;
                product.Price = updatedProduct.Price;
                product.Quantity = updatedProduct.Quantity;
            }
        }

        public List<Product> GetInventory()
        {
            return inventory;
        }
    }
}
