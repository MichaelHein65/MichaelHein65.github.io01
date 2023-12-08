function getSehenswuerdigkeiten($stadt) {
  $url = "https://de.wikipedia.org/wiki/$stadt";
  $html = file_get_contents($url);
  $dom = new DOMDocument();
  $dom->loadHTML($html);
  $bilder = $dom->getElementsByTagName('img');
  $sehenswuerdigkeiten = $dom->getElementsByTagName('p');
  $sehenswuerdigkeiten = array_map(function ($sehenswuerdigkeit) {
    return $sehenswuerdigkeit->textContent;
  }, $sehenswuerdigkeiten);
  return $sehenswuerdigkeiten;
}
