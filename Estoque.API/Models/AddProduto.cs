using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Estoque.API.Models
{
    public record AddEstoque(
        string Nome, 
        string Marca, 
        double Preco,
        DateTime ValidadeProduto
    )
    {

    }
}