@RestController
@RequestMapping("/favorites")
public class FavoriteController {
    @Autowired
    private FavoriteService service;

    @PostMapping
    public Favorite add(@RequestBody Favorite fav) {
        return service.addFavorite(fav);
    }

    @DeleteMapping("/{id}")
    public void delete(@PathVariable String id) {
        service.removeFavorite(id);
    }

    @GetMapping("/user/{userId}")
    public List<Favorite> getByUser(@PathVariable String userId) {
        return service.getFavorites(userId);
    }
}
