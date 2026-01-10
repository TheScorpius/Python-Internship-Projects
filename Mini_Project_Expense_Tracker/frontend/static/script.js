document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('expense-form');
    const list = document.getElementById('expense-list');
    const totalDisplay = document.getElementById('total-amount');
    
    // Initialize Chart
    const ctx = document.getElementById('expenseChart').getContext('2d');
    let expenseChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: [],
            datasets: [{
                data: [],
                backgroundColor: ['#ff6384', '#36a2eb', '#ffce56', '#4bc0c0', '#9966ff']
            }]
        }
    });

    // Fetch and Render Data
    async function updateUI() {
        // 1. Get Expenses List
        const res = await fetch('/api/expenses');
        const expenses = await res.json();
        
        list.innerHTML = '';
        let total = 0;

        expenses.forEach(expense => {
            total += expense.amount;
            const li = document.createElement('li');
            li.innerHTML = `
                <div class="expense-info">
                    <strong>${expense.title}</strong>
                    <span>${expense.category} • ${expense.date}</span>
                </div>
                <div class="expense-actions">
                    <strong>$${expense.amount.toFixed(2)}</strong>
                    <button class="delete-btn" onclick="deleteExpense(${expense.id})">×</button>
                </div>
            `;
            list.appendChild(li);
        });

        totalDisplay.innerText = `$${total.toFixed(2)}`;

        // 2. Get Summary for Chart
        const sumRes = await fetch('/api/summary');
        const summary = await sumRes.json();
        
        expenseChart.data.labels = Object.keys(summary);
        expenseChart.data.datasets[0].data = Object.values(summary);
        expenseChart.update();
    }

    // Add Expense
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const title = document.getElementById('title').value;
        const amount = document.getElementById('amount').value;
        const category = document.getElementById('category').value;

        await fetch('/api/expenses', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title, amount, category })
        });

        form.reset();
        updateUI();
    });

    // Delete Expense
    window.deleteExpense = async (id) => {
        if(confirm('Delete this expense?')) {
            await fetch(`/api/expenses/${id}`, { method: 'DELETE' });
            updateUI();
        }
    };

    // Initial Load
    updateUI();
});