const Router = require("express");

const UsersController = require("../controllers/UsersController");

const usersRoutes = Router();


// exemplo de middleware
function myMiddleware(request, response, next){
    const { isAdmin } = request.body;

    if(!isAdmin){
        return response.json({message: "Usuário não autorizado!"})
    }
    
    next();
}

const usersController = new UsersController();

usersRoutes.use(myMiddleware);
usersRoutes.post("/create", usersController.create);


module.exports = usersRoutes;