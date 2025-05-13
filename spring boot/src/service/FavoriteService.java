@Service
public class FavoriteService {
    @Autowired
    private FavoriteRepository repo;

    public List<Favorite> getFavorites(String userId) {
        return repo.findByUserId(userId);
    }

    public Favorite addFavorite(Favorite fav) {
        return repo.save(fav);
    }

    public void removeFavorite(String id) {
        repo.deleteById(id);
    }
}
