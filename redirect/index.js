// Permanently redirects every www.mallok.dev request to the apex domain.
export default {
  fetch(request) {
    const url = new URL(request.url);
    url.protocol = 'https:';
    url.hostname = 'mallok.dev';
    url.port = '';
    return Response.redirect(url.toString(), 301);
  },
};
