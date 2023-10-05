using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Estoque.API.Entities
{
    public class Produto
    {
        public int Id { get; private set; }
        public string Nome { get; private set; }
        public string Marca { get; private set; }
        public double Preco { get; private set; }
        public DateTime DataCadastro { get; private set; }
        public DateTime ValidadeProduto { get; private set; }
    }
}