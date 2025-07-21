function getSehenswuerdigkeiten($stadt) {
    $url = "https://de.wikipedia.org/wiki/" . urlencode($stadt);
    $html = @file_get_contents($url);
    if ($html === false) {
        return false;
    }

    libxml_use_internal_errors(true);
    $dom = new DOMDocument();
    if (!$dom->loadHTML($html)) {
        libxml_clear_errors();
        return false;
    }

    $paragraphs = $dom->getElementsByTagName('p');
    $sehenswuerdigkeiten = [];
    foreach ($paragraphs as $p) {
        $sehenswuerdigkeiten[] = $p->textContent;
    }
    libxml_clear_errors();
    return $sehenswuerdigkeiten;
}
