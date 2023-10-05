using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Estoque.API.Entities
{
    public class Produto
    {
        public Produto(string nome, string marca, double preco, DateTime validadeProduto)
        {
            Nome = nome;
            Marca = marca;
            Preco = preco;
            DataCadastro = DateTime.Now;
            ValidadeProduto = validadeProduto;
        }
        public int Id { get; private set; }
        public string Nome { get; private set; }
        public string Marca { get; private set; }
        public double Preco { get; private set; }
        public DateTime DataCadastro { get; private set; }
        public DateTime ValidadeProduto { get; private set; }

        public void UpdateProduto(string nome, string marca, double preco, DateTime validadeProduto)
        {
            Nome = nome;
            Marca = marca;
            Preco = preco;
            ValidadeProduto = validadeProduto;
        }
    }
}