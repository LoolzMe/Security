function n(s){
b=[];for(i=0;i<s.length;i+=2)b.push(parseInt(s[i]+s[i+1],16));return b}
function s(n){
d='0123456789abcdef';
r='';for(i=0;i<n.length;++i)r+=d[~~(n[i]/16)]+d[n[i]%16];return r}
c='/DDoS02/dc5e7c2b1de45649';
d=n(c.substring(8,16));
k=n(c.substring(16,24));
for(i=0;i<4;++i)d[i]^=k[i];

console.log(c.substring(0,8)+s(d)+'/.htaccess')