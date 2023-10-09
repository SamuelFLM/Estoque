using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Estoque.API.Entities;
using Microsoft.EntityFrameworkCore;

namespace Estoque.API.Persistence.Repositories
{
    public class ProdutoRepository : IProdutoRepository
    {
        private readonly ProdutoContext _context;

        public ProdutoRepository(ProdutoContext context)
        {
            _context = context;
        }

        public void Add(Produto produto)
        {
            _context.Produtos.Add(produto);
            _context.SaveChanges();
        }

        public void Delete(Produto produto)
        {
            _context.Produtos.Remove(produto);
            _context.SaveChanges();
        }

        public List<Produto> GetAll()
        {
            return _context.Produtos.AsNoTracking().ToList();
        }

        public Produto GetById(int id)
        {
            return _context.Produtos.SingleOrDefault(x => x.Id == id);
        }

        public Produto GetByProduct(string product)
        {
            return _context.Produtos.SingleOrDefault(x => x.Nome == product);
        }

        public void Update(Produto produto)
        {
           _context.Produtos.Update(produto);
            _context.SaveChanges();
        }
    }
}