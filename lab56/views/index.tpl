% rebase('layout.tpl', title='Home Page', year=year)
<br>
<form action ="/meow" method="post">
  <fieldset>
    <legend>Asking questions!</legend>
    <div class="form-group">
      <label for="exampleInputEmail1" class="form-label mt-4">Your email</label>
      <input type="email" class="form-control" id="exampleInputEmail1" name="ADDRESS" aria-describedby="emailHelp" placeholder="Enter email" required>
    </div>
    <div class="form-group">
      <label for="exampleTextarea" class="form-label mt-4">Your question</label>
      <textarea class="form-control" id="exampleTextarea" name="QUESTION" rows="3" required></textarea>
    </div>
    <br>
    <button type="submit" value="Send" class="btn btn-primary">Submit</button>
</form>