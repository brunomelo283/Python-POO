function ConfirmAnuncio(id_produto)
{
    var ans = window.confirm(`Certeza que deseja excluir o id ${id_produto}` )
    if(ans == true)
        window.location.href = `/pgHome/ExcluirAnuncio?id_produto=${id_produto}` 
}

   
