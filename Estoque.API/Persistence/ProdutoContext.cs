using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using Estoque.API.Entities;

namespace Estoque.API.Persistence
{
    public class ProdutoContext : DbContext
    {
        public ProdutoContext(DbContextOptions options) : base(options)
        {

        }
        public DbSet<Produto> Produtos { get; set; }
    }
}