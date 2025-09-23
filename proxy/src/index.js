
export default {
  async fetch(request,env) {
    const url = "https://demo-api-capital.backend-capital.com/api/v1/session";

    console.log("Incoming request method:", request.method);
    console.log("Incoming request headers:", Object.fromEntries(request.headers));

    const newRequest = new Request(url, {
      method: request.method,
      headers: request.headers,
      body: request.body,
    });

    let resp;
    try {
      resp = await fetch(newRequest);
      console.log("Fetched response status:", resp.status);
      console.log("Fetched response headers:", Object.fromEntries(resp.headers));
    } catch (err) {
      console.error("Error fetching backend:", err);
      return new Response("Error fetching backend", { status: 500 });
    }

    const headers = new Headers(resp.headers);
    headers.set("Access-Control-Allow-Origin", "*");
    headers.set("Access-Control-Allow-Methods", "GET, POST, OPTIONS");
    headers.set("Access-Control-Allow-Headers", "*");
    headers.set("Access-Control-Expose-Headers", "Content-Disposition"); // <-- important
    const contentDisposition = resp.headers.get("Content-Disposition");
    console.log("Content-Disposition from backend:", contentDisposition);
    if (contentDisposition) {
      headers.set("Content-Disposition", contentDisposition);
    }

    if (request.method === "OPTIONS") {
      return new Response(null, { headers });
    }

    return new Response(resp.body, {
      status: resp.status,
      statusText: resp.statusText,
      headers,
    });
  },
};

