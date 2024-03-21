# Things of keep in mind

Wouldn't have worked in any case that involved the cancellation of a row. Also the number of rows in the "raccolte" table is dynamic.
- Also: if raccolta==NULL => I launch the 403 error (to implement) 

Sequencing in SQLite doesn't guarantee integrity of the number progression: i.e. in the case of deleting one "raccolta" row from the table, the numbering must still increase to keep the univocity of the "raccolta".
```python
@app.route('/raccolta/<int:raccolta_id>')
def raccolta(raccolta_id):
    '''
    The following code is wrong:
    if I deleted a row from the DB, I would need to 
    '''
    # raccolte = []
    # raccolte = raccolte_dao.get_all_raccolte()

    # # Check if the provided raccolta_id is within the valid range
    # if raccolta_id < 0 or raccolta_id > len(raccolte):
        # abort(403)  # Post not found, return a 404 error

    # raccolta = raccolte[raccolta_id-1]
    # # raccolta = raccolte[raccolta_id-2]
    
    '''
    Whereas, this is the correct version of it
    '''
    raccolta = raccolte_dao.get_raccolta(raccolta_id)
```
