// 스토리지에 저장될 이름, 캐싱 할 파일 목록
var CACHE_NAME = 'ICISTS-offline';
var filesToCache = [
    '/src/',
    '/src/App.vue',
    '/src/assets',
    // '/src/assets/favicon.ico',
    // '/stc/assets/logo.png',
    // '/src/images',
    // '/src/images/192x.png',
    // '/src/images/512x.png',
    // '/src/components',
    // '/src/components/TodoHeader.vue',
    // '/src/components/TodoFooter.vue',
    // '/src/components/TodoInput.vue',
    // '/src/components/TodoList.vue'
];

self.addEventListener('install', function(event) {
    event.waitUntil(
        // 웹 자원 캐싱
        caches.open(CACHE_NAME)
        .then(function(cache) {
            // PWA 파일 넣기
            console.log('Opened cache');
            return cache.addAll(filesToCache);
        })
    )
})