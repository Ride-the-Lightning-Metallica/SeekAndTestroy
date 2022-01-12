let form = document.getElementById('searchForm')
form.addEventListener('submit', function(event) {
    event.preventDefault();
    $.ajax({
        type: 'POST',
        url: '',
        data: {
            key: $('#searchField').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        dataType: 'json',
        success: function(response) {
            render(response)
        }
    })
});


function render(data) {
    let template = Hogan.compile(html);
    let output = template.render(data);

    const div = document.querySelector('.content__inner');
    div.innerHTML = output;
}


let html = `
{{#tests}}
    <div class="content__item">
        <h4 class="content__item__title">{{ title }}</h4>
        <img
            src="media/{{ image }}"
            alt="test image"
            class="content__item__img"
        />
        <div class="content__item__information">
            <p class="content__item__author">
                Author: {{ author__username }}
            </p>
            <p class="content__item__author">
                Category: {{ category__title }}
            </p>
            <p class="content__item__description">
                {{ description }}
            </p>
            <div
                style="
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                "
            >
                <p class="content__item__complexity">
                    Complexity:
                    <span style="font-size: 17px">
                        {{ difficulty }}
                    </span>
                </p>
                <a
                    href=""
                    class="content__item__button"
                >
                    Go!
                </a>
            </div>
        </div>
    </div>
{{/tests}}`
