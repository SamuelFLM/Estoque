using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Estoque.API.Persistence;
using Estoque.API.Models;
using Microsoft.AspNetCore.Mvc;
using Estoque.API.Entities;

namespace Estoque.API.Controllers
{
    [Route("v1/produto")]
    [ApiController]
    public class EstoqueController : ControllerBase
    {
        private readonly ProdutoContext _produto;

        public EstoqueController(ProdutoContext produto)
        {
            _produto = produto;
        }


        [HttpGet]
        public IActionResult Obter()
        {
            var produtos = _produto.Produtos;
            return Ok(produtos);
        }

        [HttpGet("{id}")]
        public IActionResult ObterPorId(int id)
        {
            var produto = _produto.Produtos.SingleOrDefault(x => x.Id == id);

            if (produto == null)
                return NotFound();

            return Ok(produto);
        }

        [HttpPost]
        public IActionResult Criar(AddProduto model)
        {
            Produto produto = new Produto(
                model.Nome,
                model.Marca,
                model.Preco,
                model.ValidadeProduto
            );
            _produto.Produtos.Add(produto);

            _produto.SaveChanges();

            return CreatedAtAction(nameof(ObterPorId), new { id = produto.Id }, produto);
        }
    }
}