<form method="post" action="{% url 'your_view_name' %}">
    {% csrf_token %}
    <input type="text" name="your_field" required>
    <button type="submit">Submit</button>
</form>
