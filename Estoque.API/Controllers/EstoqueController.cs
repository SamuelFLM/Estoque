using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Estoque.API.Persistence;
using Estoque.API.Models;
using Microsoft.AspNetCore.Mvc;
using Estoque.API.Entities;
using Estoque.API.Persistence.Repositories;

namespace Estoque.API.Controllers
{
    [Route("v1/produto")]
    [ApiController]
    public class EstoqueController : ControllerBase
    {
        private readonly IProdutoRepository _repository;

        public EstoqueController(IProdutoRepository repository)
        {
            _repository = repository;
        }


        [HttpGet]
        public IActionResult GetAll()
        {
            var produtos = _repository.GetAll();
            return Ok(produtos);
        }

        [HttpGet("{id}")]
        public IActionResult GetById(int id)
        {
            var produto = _repository.GetById(id);

            if (produto == null)
                return NotFound();

            return Ok(produto);
        }

        [HttpGet("GetByProduct")]
        public IActionResult GetByProduct(string produto)
        {
            var item = _repository.GetByProduct(produto);
            return Ok(item);
        }

        [HttpPost]
        public IActionResult Post(AddProduto model)
        {
            Produto produto = new Produto(
                model.Nome,
                model.Marca,
                model.Preco,
                model.ValidadeProduto
            );

            _repository.Add(produto);

            return CreatedAtAction(nameof(GetById), new { id = produto.Id }, produto);
        }

        [HttpPut("{id}")]
        public IActionResult Put(int id, UpdateProduto model)
        {
            var produto = _repository.GetById(id);

            if (produto == null)
                return NotFound();

            if (model.ValidadeProduto == DateTime.MinValue)
                return BadRequest();

            produto.UpdateProduto(model.Nome, model.Marca, model.Preco, model.ValidadeProduto);

            _repository.Update(produto);

            return NoContent();
        }

        [HttpDelete("{id}")]
        public IActionResult Delete(int id)
        {
            var produto = _repository.GetById(id);

            if (produto == null)
                return NotFound();

            _repository.Delete(produto);

            return NoContent();
        }
    }
}