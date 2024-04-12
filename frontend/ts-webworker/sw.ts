const scope = self as unknown as ServiceWorkerGlobalScope;

async function cache(resources: string[]) {
    const storage = await caches.open("data");
    await storage.addAll(resources)
}

scope.addEventListener('install', event => {
    event.waitUntil(
        cache([
            "/",
            "/static/scripts/main.js",
            "/static/styles.css",
        ])
    );
});

scope.addEventListener('fetch', event => {
    event.respondWith(caches.match(event.request)
        .then(response => {
            if (response !== undefined) return response;
            return fetch(event.request)
        })
    );
})
