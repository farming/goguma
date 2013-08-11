//D3 initialize
var width = 1960,
    height = 1080;

var nodes = [
], links = [
];

var idtable = {};

var force = d3.layout.force()
        .size([width, height])
        .nodes(nodes)
        .links(links)
        .gravity(.05)
        .linkDistance(30)
        .distance(300)
        .charge(-60)
        .start();

var svg = d3.select('.pagetree').append('svg')
        .attr('width', width)
        .attr('height', height);

force.on("tick", function() {
    var link = svg.selectAll('.link'),
        node = svg.selectAll('.node');

    link.attr("x1", function(d) { return d.source.x; })
        .attr("y1", function(d) { return d.source.y; })
        .attr("x2", function(d) { return d.target.x; })
        .attr("y2", function(d) { return d.target.y; });

    node.attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });
});

function restart() {
    var node = svg.selectAll('.node')
            .data(force.nodes())
            .enter().append('g')
            .attr('class', 'node')
            .call(force.drag);

    node.append('image')
        .attr('xlink:href', function(d, i) { return d.src; })
        .attr('x', -8)
        .attr('y', -8)
        .attr('width', 64)
        .attr('height', 64);

    node.append('text')
        .attr('dx', 12)
        .attr('dy', '0.35em')
        .text(function(d) { return d.url; });

    var link = svg.selectAll('.link')
            .data(force.links())
            .enter().append('line')
            .attr('class', 'link');

    force.start();
};

//Socket.IO binding
var socket = io.connect('/pagegen');
socket.on('pageimg_rep', function(response) {
    response = JSON.parse(response);
    idtable[response.id] = nodes.length;
    if (response.parentid in idtable) {
        links.push({
            source: idtable[response.id],
            target: idtable[response.parentid]
        });
    }
    nodes.push({
        src: response.src,
        url: response.url
    });
    restart();
});

socket.emit('pageimg_ask', $('.pagetree').data('url'));
