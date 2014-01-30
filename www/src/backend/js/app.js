var ENTER_KEY = 13;

Backbone.View.prototype.close = function(){
  this.remove();
  this.unbind();
  
  if (this.onClose){
    this.onClose();
  }
  
}

$(function() {
    new app.router();
    Backbone.history.start();
    
});

app.showView = function(view) {
    if (this.currentView){
      this.currentView.close();
    }
 
    this.currentView = view;
    this.currentView.render();    
 
    $("#app_container").html(this.currentView.el);  
}

app.showProject = function(id){
    
    this.showView(new app.view.ProjectView({
        model: new app.model.Project({
            "id": id
        })
    }));
};
