import './Restaurant.css'
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function RestaurantTable() {
    const url = "http://localhost:4000";

    const [rows, setRows] = useState([])
    const [add_row, setAddRow] = useState(false)
    const [edit_row, setEditRow] = useState(false)
    const [edit_row_id, setRowId] = useState()

    const fetchInfo = () => {
        try {
            axios.get('http://localhost:4000')
            .then((res) =>{
                setRows(res.data.all);
            })
        } catch (error) {
            console.error(error)
        }
    
    }
    
    useEffect(() => {
    fetchInfo()
    }
    , []);

    const deleteRow = (Id) => {
        console.log(Id)
        // const rowIdToDelete = 
    fetch(`${url}/${Id}`, {
    method: 'DELETE',
    body: JSON.stringify()
    }).then(fetchInfo)
              
  };

    const addRow = () => {
        setAddRow(false)
        const f_n = document.getElementById('1')
        const l_n = document.getElementById('2')
        const  p_n = document.getElementById('3')
        const e = document.getElementById('4')
        const r = document.getElementById('5')
        const newS = {
            first_name: f_n.value, last_name: l_n.value, phon_number: p_n.value, email: e.value, role: r.value
        }
        console.log(newS)
        fetch(url, {
        method: 'POST',
        headers: { "Content-Type":"application/json" },
        body: JSON.stringify(newS)
    }).then((res) => {
        res.json()
    }).then((data) => {
        console.log(data)
        fetchInfo();
    })
};

    const editRow = (id) => {
        setEditRow(true)
        setRowId(id)
    } 

    const saveRow = (id) => {
        setEditRow(false)
        setRowId()
    }
    
    return (
        <div className='RestaurantTable'>
        

        <table>
            <thead>
                <tr>
                    <th>First Name</th>
                    <th>Last Name</th>
                    <th>Phone Number</th>
                    <th>Email</th>
                    <th>Role</th>
                </tr>
                </thead>
                <tbody>
                {rows.map((row, index) => {
                    return (
                        <tr key = {index}>
                            {<td>{row.first_name}</td>}
                            {<td>{row.last_name}</td>}
                            {<td>{row.phon_number}</td>}
                            {<td>{row.email}</td>}
                            {<td>{row.role}</td>}
                            {/* {edit_row && edit_row_id===row.ID <th>first_name</t} */}
                            <td><button className='del-btn' onClick={() => deleteRow(row.ID)}>Delete</button></td>
                            {!edit_row && <td><button className='edit-btn' onClick={() => editRow(row.ID)}>Edit</button></td>}
                            {edit_row && <td><button className='save-btn' onClick={() => saveRow(row.ID)}>Save</button></td>}

                        </tr>
                    )
                })}
                </tbody>
                
        </table>
        {add_row && <div className='input-row'>
            <th>First Name</th>
            <input type='text' id='1'/>
            <th>Last Name</th>
            <input type='text' id='2'/>
            <th>Phone Number</th>
            <input type='number' id='3'/>
            <th>Email</th>
            <input type='email' id='4'/>
            <th>Role</th>
            <input type='text' id='5'/>
            <button className='save-btn' onClick={() => addRow()}>Save</button>
            <button className='close-btn' onClick={() => setAddRow(false)}>Close</button>
            </div>}
        <button className="add-btn" onClick={() => setAddRow(true)}>Add Row</button>

    </div>
    );
}

export default RestaurantTable;