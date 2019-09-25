import functools

def element_as_list_item(element):
    if hasattr(element.dialogue, "persona"):
        return f"""
<li style="animation-duration: {element.duration}s; animation-delay: {element.offset}s">
<blockquote class="line">
{'<header class="persona"> {{ 0.dialogue.persona.name.firstname }} {{ 0.dialogue.persona.name.surname }} </header>'.format(element)
if hasattr(element.dialogue.persona, "name") else ""}
<p class="speech">{ element.dialogue.text }</p>
</blockquote>
</li>
        """
    elif hasattr(element.dialogue, "loop"):
        return """
<li>
<audio
    src="/audio/{0.dialogue.resource}"
    autoplay="autoplay" preload="auto"
>
</audio>
</li>
        """.format(element)
    else:
        return ""


def body_to_html(location="", frame=[], sep="\n"):
    return f"""
<main class="grid-front">
<h1>{location.capitalize()}</h1>
<ul class="mod-dialogue">
{{0}}
</ul>
</main>
<nav class="grid-steer">
<form role="form" action="/1234" method="post" name="choice" >
    <button type="submit">Choose 1234</button>
</form>
</nav>
<section class="grid-dash">
</section>"""


@functools.lru_cache()
def base_to_html(refresh=None):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
{'<meta http-equiv="refresh" content="{0}">'.format(refresh) if refresh is not None else ''}
<meta http-equiv="X-UA-Compatible" content="ie=edge">
<link rel="stylesheet" href="/css/blmst.css" />
</head>
<body>
{{0}}
</body>
</html>"""
