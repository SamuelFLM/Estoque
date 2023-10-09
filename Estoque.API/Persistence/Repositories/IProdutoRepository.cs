using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Estoque.API.Entities;

namespace Estoque.API.Persistence.Repositories
{
    public interface IProdutoRepository
    {
        List<Produto> GetAll();
        Produto GetById(int id);

        Produto GetByProduct(string product);
        void Add(Produto produto);
        void Update(Produto produto);
        void Delete(Produto produto);
    }
}